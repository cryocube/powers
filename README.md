# Powers
Powers is a local python3 program which is intended as a proof of concept for a separate more robust program.<br>
The intention is to allow easy query and data location of powers available to players in the player facing rulebook of the Shadow Accord LARP operated by NWLARPers.<br>
http://nwlarpers.org/

## Current Capabilities
At its root, the software is capabable of showing all unique instances of a power, in the Shadow Accord Rulebook using the following information:
* Power Name
* Tree Name
* Power Type
* Meta Type
* ST_Only Powers
* Breachable Powers

## Backend
Powers is designed using Python3 and SQLite.  

### Abandoned Features
* Values for Power Name and Tree Name to be 'like' - Will be superceeded by dynamic query creation

### Stage 1 To Do List: The De-Brittling  [ACHIEVED WITH AUTHORITY]
* [X] Break out SQL queries to separate Variable
* [X] Input Sanitization
* [X] Validation Dictionary for Type and Meta Type

### Stage 2 To Do List: Look Ma! NO HANDS!
* [ ] Convert to web version using Bottle or Flask

### Stage 3: Moar Bendy
* [ ] Transition to SQL Alchemy for more dynamism

### Stage 4: Share the load
* [ ] Demo to Org

### Long Term Software Goals
* [ ] Ability to enter a number of powers and get a list of 3x5 power cards printed for quick in game reference
* [ ] GUI on Web
* [ ] Dynamic Query Generation
* [ ] A Pony
