create table items (
    id int not null,
    item varchar(255), 
    description varchar(4000),
    primary key(id)
);

create table abilities (
    id serial not null,
    ability varchar(255), 
    description varchar(4000),
    primary key(id)
);

create table natures (
    id serial not null,
    nature varchar(255), 
    attack varchar(10),
    defense varchar(10),
    spattack varchar(10),
    spdefense varchar(10),
    speed varchar(10),
    primary key(id)
);

create table moves (
    id int not null,
    move varchar(255), 
    description varchar(255),
    type varchar(255),
    category varchar(255),
    power varchar(255),
    accuracy varchar(255),
    pp varchar(255),
    zeffect varchar(255),
    priority varchar(255),
    crit varchar(255),
    primary key(id)
);

create table pokemons (
    id int not null,
    ndex varchar(255), 
    species varchar(255),
    forme varchar(255),
    type1 varchar(255),
    type2 varchar(255),
    ability1 varchar(255),
    ability2 varchar(255),
    abilityH varchar(255),
    hp varchar(30),
    attack varchar(30),
    defense varchar(30),
    spattack varchar(30),
    spdefense varchar(30),
    speed varchar(30),
    total varchar(30),
    weight varchar(30),
    height varchar(30),
    dex1 varchar(30),
    dex2 varchar(30),
    class varchar(80),
    percentmale varchar(30),
    percentfemale varchar(30),
    preevolution varchar(30),
    egggroup1 varchar(100),
    egggroup2 varchar(100),
    primary key(id)
);

