-- SQLite

drop table sentiment

create table sentiment ('id' TEXT, 
                        'sentence' TEXT, 
                        'logit' TEXT, 
                        'prediction' TEXT, 
                        'sentiment_score' REAL)


SELECT count(*) from sentiment;


select * from sentiment where sentiment_score > .85

select DISTINCT id from sentiment


VACUUM;