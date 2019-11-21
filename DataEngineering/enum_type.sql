
CREATE TYPE rating_enum AS ENUM (
    'Great', 'Good', 'Average', 'Bad', 'Awful') ;
	
select * from pg_catalog.pg_enum;

alter table reviews alter column rating type rating_enum using rating::rating_enum;
	

