import stats

# Enumerated constants for the item types.
GENERIC, SWORD, AXE, MACE, DAGGER, STAFF, BOW, POLEARM, ARROW, SHIELD, SLING, \
    BULLET, CLOTHES, LIGHT_ARMOR, HEAVY_ARMOR, HAT, HELM, GLOVE, GAUNTLET, \
    SANDALS, SHOES, BOOTS, CLOAK = range( 23 )

class Item( object ):
    true_name = "Item"
    true_desc = ""
    statline = stats.StatMod()
    itemtype = GENERIC
    identified = False
    attackdata = None
    quantity = 0
    avatar_image = None
    avatar_frame = 0
    mass = 1
    def cost( self ):
        it = 1
        if self.statline != None:
            it += self.statline.cost()
        return it

class NormalCloak( Item ):
    true_name = "Cloak"
    true_desc = "A warm grey cloak."
    itemtype = CLOAK
    avatar_image = "avatar_cloak.png"
    avatar_frame = 0
    mass = 10

class ThiefCloak( NormalCloak ):
    true_name = "Thief Cloak"
    true_desc = "A dark cloak to help you hide in shadows."
    avatar_frame = 4
    statline = stats.StatMod({ stats.STEALTH: 5 })

class NormalClothes( Item ):
    true_name = "Peasant Garb"
    true_desc = ""
    itemtype = CLOTHES
    avatar_image = "avatar_cloak.png"
    avatar_frame = 0
    statline = stats.StatMod({ stats.PHYSICAL_DEFENSE: 5 })
    mass = 20

class LeatherArmor( Item ):
    true_name = "Leather Armor"
    true_desc = ""
    itemtype = LIGHT_ARMOR
    avatar_image = "avatar_cloak.png"
    avatar_frame = 0
    statline = stats.StatMod({ stats.PHYSICAL_DEFENSE: 10 })
    mass = 90

class ChainmailArmor( Item ):
    true_name = "Chainmail Armor"
    true_desc = ""
    itemtype = HEAVY_ARMOR
    avatar_image = "avatar_cloak.png"
    avatar_frame = 0
    statline = stats.StatMod({ stats.PHYSICAL_DEFENSE: 20, stats.MAGIC_ATTACK: -20, stats.STEALTH: -10 })
    mass = 250


if __name__ == '__main__':
    tc = ThiefCloak()
    nc = NormalClothes()
    la = LeatherArmor()
    ca = ChainmailArmor()

    print tc.cost()
    print nc.cost()
    print la.cost()
    print ca.cost()



