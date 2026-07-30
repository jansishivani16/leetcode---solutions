select id, movie, description, rating
from Cinema
where description <> "boring"
    AND id % 2 = 1
Order by rating DESC;