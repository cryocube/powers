SELECT *
from innate_tree 
join factions on innate_tree.subfaction_id=factions.subfaction_id
join trees on trees.tree_id=innate_tree.tree_id
join power_trees on power_trees.tree_id=trees.tree_id
join powers on powers.power_id=power_trees.power_id