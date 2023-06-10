-- question 1: show all tables and explain how they are related to one another:
/* The art_museum database is related in various ways. The primary key in art_object called 
   'id_no' is a foreign key in many other tables which aids us in identifying the art_objects more 
	efficiently. Another example would be the borrowed_from table where the collection_name is a key
	from the collection table as all art objects in the collection are borrowed items. For update/delete
    trigger we added on update/delete cascade so that when a change is made in one table, it also changes
    in another table with that attribute */
USE art_museum;
SHOW TABLES;
select * from art_object;
select * from artist;
select * from borrowed;
select * from borrowed_from;
select * from collection;
select * from exhibition;
select * from other;
select * from painting;
select * from permanent_collection;
select * from sculpture;
select * from statue;

-- question 2: retrieve object title and exhibition name where epoch is renaissance and object description is statue
SELECT id_no, object_title, exhibition
FROM art_object 
WHERE epoch = 'Renaissance' AND object_description = 'statue';

-- question 3: retrieval query with ordered artist_name
SELECT artist_name, epoch, artist_description 
FROM artist
ORDER BY artist_name; 

-- question 4: nested retrieval query that retrieve id_no and artist name when material in statue is bronze
SELECT id_no, artist_name
FROM art_object
WHERE id_no IN
    (SELECT id_no
    FROM statue
    WHERE material = 'Bronze');

-- question 5: retrieve artist name, object_title, paint_type and drawn_on using Joining
use art_museum;
select a.artist_name,a.object_title , p.paint_type, p.drawn_on
FROM art_object as a
RIGHT OUTER JOIN painting as p
ON a.id_no = p.id_no
GROUP BY a.artist_name;

-- question 6: updates every id_no 003 to 100 for all tables
use art_museum;
UPDATE art_museum.art_object as a
SET a.id_no  = '100'  
WHERE a.id_no = '003';

-- question 7: delete every id_no 001 from all tables
DELETE
FROM art_object
WHERE id_no = '001';
