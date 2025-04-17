OPTIONS (SKIP=1)
LOAD DATA
INFILE 'myterror.csv'
INTO TABLE myterror
FIELDS TERMINATED BY ','
TRAILING NULLCOLS (
    eventid,
    iyear,
    imonth,
    iday,
    country,
    country_txt,
    region,region_txt,
    provstate,
    city,
    latitude,
    longitude
)