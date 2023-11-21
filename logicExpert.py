from typing import ClassVar

from connection_data import area_doors_unpackable
from door_logic import canOpen
from item_data import items_unpackable, Items
from loadout import Loadout
from logicInterface import AreaLogicType, LocationLogicType, LogicInterface
from logic_shortcut import LogicShortcut

# TODO: There are a bunch of places where where Expert logic needed energy tanks even if they had Varia suit.
# Need to make sure everything is right in those places.
# (They will probably work right when they're combined like this,
#  but they wouldn't have worked right when casual was separated from expert.)

# TODO: There are also a bunch of places where casual used icePod, where expert only used Ice. Is that right?

(
    CraterR, SunkenNestL, RuinedConcourseBL, RuinedConcourseTR, CausewayR,
    SporeFieldTR, SporeFieldBR, OceanShoreR, EleToTurbidPassageR, PileAnchorL,
    ExcavationSiteL, WestCorridorR, FoyerR, ConstructionSiteL, AlluringCenoteR,
    FieldAccessL, TransferStationR, CellarR, SubbasementFissureL,
    WestTerminalAccessL, MezzanineConcourseL, VulnarCanyonL, CanyonPassageR,
    ElevatorToCondenserL, LoadingDockSecurityAreaL, ElevatorToWellspringL,
    NorakBrookL, NorakPerimeterTR, NorakPerimeterBL, VulnarDepthsElevatorEL,
    VulnarDepthsElevatorER, HiveBurrowL, SequesteredInfernoL,
    CollapsedPassageR, MagmaPumpL, ReservoirMaintenanceTunnelR, IntakePumpR,
    ThermalReservoir1R, GeneratorAccessTunnelL, ElevatorToMagmaLakeR,
    MagmaPumpAccessR, FieryGalleryL, RagingPitL, HollowChamberR, PlacidPoolR,
    SporousNookL, RockyRidgeTrailL, TramToSuziIslandR
) = area_doors_unpackable

(
    Missile, Super, PowerBomb, Morph, Springball, Bombs, HiJump,
    GravitySuit, Varia, Wave, SpeedBooster, Spazer, Ice, Grapple,
    Plasma, Screw, Charge, SpaceJump, Energy, Reserve, Xray
) = items_unpackable

energy200 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Energy) >= 1
))

energy300 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Energy) >= 2
))
energy400 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Energy) >= 3
))
energy500 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Energy) >= 4
))
energy600 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Energy) >= 5
))
energy700 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Energy) >= 6
))
energy800 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Energy) >= 7
))
energy900 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Energy) >= 8
))
energy1000 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Energy) >= 9
))
energy1200 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Energy)  >= 11
))
energy1500 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Energy)  >= 14
))


hellrun1 = LogicShortcut(lambda loadout: (
    (Varia in loadout) or
    (energy200 in loadout)
))
hellrun2 = LogicShortcut(lambda loadout: (
    (Varia in loadout) or
    (energy300 in loadout)
))
hellrun3 = LogicShortcut(lambda loadout: (
    (Varia in loadout) or
    (energy400 in loadout)
))
hellrun4 = LogicShortcut(lambda loadout: (
    (Varia in loadout) or
    (energy500 in loadout)
))
hellrun5 = LogicShortcut(lambda loadout: (
    (Varia in loadout) or
    (energy600 in loadout)
))
hellrun6 = LogicShortcut(lambda loadout: (
    (Varia in loadout) or
    (energy700 in loadout)
))
hellrun8 = LogicShortcut(lambda loadout: (
    (Varia in loadout) or
    (energy900 in loadout)
))
hellrun9 = LogicShortcut(lambda loadout: (
    (Varia in loadout) or
    (energy1000 in loadout)
))
hellrun11 = LogicShortcut(lambda loadout: (
    (Varia in loadout) or
    (energy1200 in loadout)
))
hellrun14 = LogicShortcut(lambda loadout: (
    (Varia in loadout) or
    (energy1500 in loadout)
))

missile10 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Missile) * 5 >= 10
))
missile15 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Missile) * 5 >= 15
))
super10 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Super) * 5 >= 10
))
super30 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Super) * 5 >= 30
))
powerBomb10 = LogicShortcut(lambda loadout: (
    (Morph in loadout) and
    loadout.count(Items.PowerBomb) >= 2
))
powerBomb15 = LogicShortcut(lambda loadout: (
    (Morph in loadout) and
    loadout.count(Items.PowerBomb) >= 3
))
canCF = LogicShortcut(lambda loadout: (
    (Morph in loadout) and
    (loadout.count(Items.PowerBomb) >= 3) and
    (super10 in loadout) and
    (missile10 in loadout)
))
canUseBombs = LogicShortcut(lambda loadout: (
    (Morph in loadout) and
    ((Bombs in loadout) or (PowerBomb in loadout))
))
canUsePB = LogicShortcut(lambda loadout: (
    (Morph in loadout) and
    (PowerBomb in loadout)
))
canIBJ = LogicShortcut(lambda loadout: (
    (Morph in loadout) and
    (Bombs in loadout)
))
canBreakBlocks = LogicShortcut(lambda loadout: (
    #with bombs or screw attack, maybe without morph
    (canUseBombs in loadout) or
    (Screw in loadout)
))
pinkDoor = LogicShortcut(lambda loadout: (
    (Missile in loadout) or
    (Super in loadout)
))
kraid = LogicShortcut(lambda loadout: (
    (canUsePB in loadout) and
    (
        (pinkDoor in loadout) or
        (Charge in loadout)
        )
))
back = LogicShortcut(lambda loadout: (
    (Morph in loadout) and
    (
        (canIBJ in loadout) or
        (Springball in loadout) or
        (kraid in loadout)
        )
))

area_logic: AreaLogicType = {
    "Early": {
        # using SunkenNestL as the hub for this area, so we don't need a path from every door to every other door
        # just need at least a path with sunken nest to and from every other door in the area
        ("CraterR", "SunkenNestL"): lambda loadout: (
            True
        ),
        ("SunkenNestL", "CraterR"): lambda loadout: (
            True
        ),
        ("SunkenNestL", "RuinedConcourseBL"): lambda loadout: (
            True
        ),
        ("SunkenNestL", "RuinedConcourseTR"): lambda loadout: (
            True
            # TODO: Expert needs energy and casual doesn't? And Casual can do it with supers, but expert can't?
        ),   
    },
}


location_logic: LocationLogicType = {
    "Morph Ball": lambda loadout: (
        True
    ),
    "Bombs": lambda loadout: (
        (canUseBombs in loadout)
    ),
    "Accumulator Beam": lambda loadout: (
        (canUseBombs in loadout)
    ),
    "Kraid Power Bomb": lambda loadout: (
        (kraid in loadout)
    ),
    "Alpha Super Missile": lambda loadout: (
        (canUsePB in loadout) and
        (
            (Ice in loadout) or
            (SpaceJump in loadout) or
            (
                (canIBJ in loadout) and
                (
                    (Super in loadout) or
                    (Screw in loadout)
                    )
                )
            )
    ),
    "Accumulator Reserve Tank": lambda loadout: (
        (Morph in loadout) and
        (pinkDoor in loadout)
    ),
    "Trove Super Missile": lambda loadout: (
        (Morph in loadout) and
        (Super in loadout)
    ),
    "Trove Reserve Tank": lambda loadout: (
        (Morph in loadout)
    ),
    "Trove Energy Tank": lambda loadout: (
        (Morph in loadout) and
        (pinkDoor in loadout)
    ),
    "Kraid Super Missile": lambda loadout: (
        (kraid in loadout) and
        (Super in loadout)
    ),
    "Springball": lambda loadout: (
        (canUsePB in loadout) and
        (pinkDoor in loadout)
    ),
    "Spring Top Missile": lambda loadout: (
        (canUsePB in loadout) and
        (pinkDoor in loadout)
    ),
    "Spring Low Missile": lambda loadout: (
        (canUsePB in loadout) and
        (pinkDoor in loadout)
    ),
    "Bomb Energy Tank": lambda loadout: (
        (canUseBombs in loadout)
    ),
    "Trove Bottom Missile": lambda loadout: (
        (Morph in loadout)
    ),
    "Trove Basement Missile": lambda loadout: (
        (Morph in loadout)
    ),
    "Ceiling Energy Tank": lambda loadout: (
        (back in loadout)
    ),
    "Floor Missile": lambda loadout: (
        (back in loadout) and
        (canUsePB in loadout)
    ),
    "Supa Suit": lambda loadout: (
        (back in loadout) and
        (canUsePB in loadout)
    ),
    "Crater Energy Tank": lambda loadout: (
        (back in loadout) and
        (
            (HiJump in loadout) or
            (canIBJ in loadout) or
            (
                (Morph in loadout) and
                (Springball in loadout)
                ) or
            (SpaceJump in loadout)
            )
    ),
    "Sky Missile": lambda loadout: (
        (back in loadout) and
        (canUsePB in loadout)
    ),
    "Ship Entry Missile": lambda loadout: (
        (back in loadout) and
        (canUsePB in loadout)
    ),
    "Gravity Boots": lambda loadout: (
        (back in loadout) and
        (canUsePB in loadout)
    ),
    "Ship Power Bomb": lambda loadout: (
        (back in loadout) and
        (canUsePB in loadout) and
        (pinkDoor in loadout)
    ),
    "Space Beam": lambda loadout: (
        (back in loadout) and
        (canUsePB in loadout)
    ),
    "Wave Energy Tank": lambda loadout: (
        (back in loadout) and
        (canUsePB in loadout)
    ),
    "Ship Low Missile": lambda loadout: (
        (back in loadout) and
        (canUsePB in loadout)
    ),
    "Paralyzer Beam": lambda loadout: (
        (back in loadout) and
        (canUsePB in loadout) and
        (Wave in loadout) and
        (pinkDoor in loadout)
    ),
    "Green Gate Super": lambda loadout: (
        (back in loadout) and
        (canUsePB in loadout) and
        (Super in loadout)
    ),
    "Green Gate Energy Tank": lambda loadout: (
        (back in loadout) and
        (canUsePB in loadout) and
        (Super in loadout)
    ),
    "Gravity Suit": lambda loadout: (
        (back in loadout) and
        (canUsePB in loadout) and
        (Super in loadout)
    ),


}


class Expert(LogicInterface):
    area_logic: ClassVar[AreaLogicType] = area_logic
    location_logic: ClassVar[LocationLogicType] = location_logic

    @staticmethod
    def can_fall_from_spaceport(loadout: Loadout) -> bool:
        return True
