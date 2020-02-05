select * from jobmarket_job where type like 'Contract/Permanent';
select * from jobmarket_job where type like 'Part Time/Temporary/Seasonal';

update jobmarket_job set type = 'Part Time/Temporary/Seasonal' where type like 'Part Time/Temporary/Seasonal';
update jobmarket_job set type = 'Contract/Permanent' where type like 'Contract/Permanent';