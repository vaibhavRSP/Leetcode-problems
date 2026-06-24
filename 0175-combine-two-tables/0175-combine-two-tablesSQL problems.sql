select firstname, lastname, city, state
from Person
left join address on Person.PersonID = address.personID