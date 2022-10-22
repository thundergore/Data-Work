--hackerranks '15 days of interviews' sql problem

select cte4.submission_date
     , cte4.h_count
     , ste2.hacker_id
     , ste2.name
from (
     select cte2.submission_date
          , count(hacker_id) as h_count
     from (
          select *
               , row_number() over (partition by hacker_id order by submission_date) as r_n_1
          from (
               select distinct hacker_id
                             , submission_date
               from submissions
               ) cte1
          ) cte2
              inner join (
                         select submission_date
                              , row_number() over (order by submission_date) as r_n_2
                         from (
                              select distinct submission_date
                              from submissions
                              ) cte3
                         ) cte4
                         on cte2.submission_date = cte4.submission_date and cte2.r_n_1 = cte4.r_n_2
     group by cte2.submission_date
     ) cte4
         join (
              select *, dense_rank() over (partition by submission_date order by s_tot desc, hacker_id asc) as r_n
              from (
                   select s.submission_date
                        , s.hacker_id
                        , h.name
                        , count(s.submission_id) as s_tot
                   from submissions s
                            join hackers h
                                 on s.hacker_id = h.hacker_id
                   group by s.submission_date, s.hacker_id, h.name
                   ) ste1
              ) ste2
              on ste2.submission_date = cte4.submission_date
where ste2.r_n = 1
;
