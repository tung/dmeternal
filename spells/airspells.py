from base import SOLAR, EARTH, WATER, FIRE, AIR, LUNAR, Spell
import effects
import targetarea
import enchantments
import animobs
import stats
import invocations

# CIRCLE ONE

AIR_ARMOR = Spell( "Shield of Wind",
    "Increases the physical and magical defense of all allies within 6 tiles by +5%. This effect lasts until the end of combat.",
    effects.TargetIsAlly( on_true = (
        effects.Enchant( enchantments.AirArmor, anim=animobs.BlueSparkle )
    ,) ), rank=1, gems={AIR:1}, com_tar=targetarea.SelfCentered() )

PROBE = Spell( "Probe",
    "This spell reveals secret knowledge about one target creature.",
    effects.NoEffect( anim=animobs.BlueSparkle, children = (
        effects.Probe()
    ,) ), rank=1, gems={AIR:1}, mpfudge=-1, com_tar=targetarea.SingleTarget(), exp_tar=targetarea.SingleTarget() )

# CIRCLE TWO

# CIRCLE THREE

THUNDER_STRIKE = Spell( "Thunder Strike",
    "A bolt of lightning strikes all in its path for 3d6 damage.",
    effects.OpposedRoll( on_success = (
        effects.HealthDamage( (3,6,0), stat_bonus=stats.INTELLIGENCE, element=stats.RESIST_LIGHTNING, anim=animobs.Spark )
    ,), on_failure = (
        effects.HealthDamage( (1,8,0), stat_bonus=None, element=stats.RESIST_LIGHTNING, anim=animobs.Spark )
    ,) ), rank=3, gems={AIR:1}, com_tar=targetarea.Line(), ai_tar=invocations.vs_enemy )

