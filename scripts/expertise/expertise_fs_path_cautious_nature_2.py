import sys

def addExpertisePoint(core, actor):

	player = actor.getSlottedObject('ghost')

	if not player:
		return

	if not player.getProfession() == 'force_sensitive_1a':
		return

	actor.addSkill('expertise_fs_path_cautious_nature_2')

	core.skillModService.addSkillMod(actor, 'expertise_stance_constitution', 10)
	core.skillModService.addSkillMod(actor, 'expertise_stance_parry', 1)
	core.skillModService.addSkillMod(actor, 'expertise_stance_evasion', 1)

	addAbilities(core, actor, player)

	return

def removeExpertisePoint(core, actor):

	player = actor.getSlottedObject('ghost')

	if not player:
		return

	if not player.getProfession() == 'force_sensitive_1a':
		return

	actor.removeSkill('expertise_fs_path_cautious_nature_2')

	core.skillModService.deductSkillMod(actor, 'expertise_stance_constitution', 10)
	core.skillModService.deductSkillMod(actor, 'expertise_stance_parry', 1)
	core.skillModService.deductSkillMod(actor, 'expertise_stance_evasion', 1)

	removeAbilities(core, actor, player)

	return

# this checks what abilities the player gets by level, need to also call this on level-up
def addAbilities(core, actor, player):


	return

def removeAbilities(core, actor, player):


	return
