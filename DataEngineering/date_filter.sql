select * from jobmarket_job where id>=52120 limit 50;
select count(*) from jobmarket_job where created_date > '2020-01-27'::date;
select * from jobmarket_job where title like 'Cyber Security Consultant' and created_date > '2020-01-27'::date;

select count(*) from jobmarket_job where created_date > now() - interval '15 days';