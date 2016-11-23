create table items (
    id int not null,
    item varchar(255), 
    description varchar(4000),
    primary key(id)
);

create table abilities (
    id int not null,
    ability varchar(255), 
    description varchar(4000),
    primary key(id)
);