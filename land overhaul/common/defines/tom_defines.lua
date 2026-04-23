 -- Resources
NDefines.NProduction.MAX_EQUIPMENT_RESOURCES_NEED = 4

 -- Army Fuel
NDefines.NMilitary.SURPLUS_SUPPLY_RATIO_FOR_ZERO_FUEL_FLOW = 1
NDefines.NMilitary.OUT_OF_FUEL_EQUIPMENT_MULT = 0.25
NDefines.NMilitary.FUEL_CAPACITY_DEFAULT_HOURS = 144

 -- Railway Conversion
NDefines.NSupply.RAILWAY_CONVERSION_COOLDOWN = 6
NDefines.NSupply.RAILWAY_CONVERSION_COOLDOWN_CORE = 3

 -- Commander Traits & Levels
NDefines.NMilitary.UNIT_LEADER_USE_NONLINEAR_XP_GAIN = false
NDefines.NMilitary.MAX_RELATIVE_COMBAT_DAMAGE_TO_MODIFY_XP = 10
NDefines.NMilitary.XP_GAIN_FACTOR_FOR_MAX_RELATIVE_COMBAT_DAMAGE = 10
NDefines.NMilitary.FIELD_MARSHAL_ARMY_BONUS_RATIO = 1
NDefines.NMilitary.FIELD_MARSHAL_XP_RATIO = 0.5
NDefines.NMilitary.UNIT_LEADER_INITIAL_TRAIT_SLOT = { 				-- trait slot for 0 level leader
		2.0, -- field marshal
		0.0, -- corps commander
		1.0, -- navy general
		0.0, -- operative
	}
NDefines.NMilitary.UNIT_LEADER_TRAIT_SLOT_PER_LEVEL = { 			-- num extra traits on each level
		1.0, -- field marshal
		1.0, -- corps commander
		0.5, -- navy general
		0.5, -- operative
	}