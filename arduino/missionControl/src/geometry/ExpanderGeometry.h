#include "../controls/SwitchExpander.h"

char* exp0Switches[16] = {
    // BOOSTER 
    "SPS",
    "unused",
    "unused",
    "unused",

    // CRYOGENICS
    "O2Fan",
    "H2Fan",
    "Pumps",
    "Heat",

    // BOOSTER
    "TEI",
    "TLI",
    "S-IC",
    "S-II",
    "S-iVB",
    "M-I",
    "M-II",
    "M-III"
};

char* exp1Switches[16] = {
    // PYROTECHNICS
    "MainDeploy",
    "DrogueDeploy",
    "CSM/LVDeploy",
    "CanardDeploy",
    "SM/CMDeploy",
    "ApexCoverJettsn",
    "LesMotorFire",

    "unused",

    // CONTROL
    "DockingProbe",
    "GlycolPump",
    "SCEPower",
    "WasteDump",
    "CabinFan",
    "H2OFlow",
    "IntLights",
    "SuitComp"
};

char* exp2Switches[16] = {
    // ABORT
    "ArmAbort",
    "Abort",

    // CAPCOM
    "PTT",

    // C&WS
    "MasterAlarm",
    "Lamp",
    "Ack",
    "Power",
    "Mode",

    "unused",
    "unused",
    "unused",
    "unused",
    "unused",
    "unused",
    "unused",
    "unused"
};

char* exp3Switches[16] = {
    // EVENT SEQUENCE
    "ES1",
    "ES2",
    "ES3",
    "ES4",
    "ES5",
    "ES6",
    "ES7",
    "ES8",
    "ES9",
    "ES10",

    "unused",
    "unused",
    "unused",
    "unused",
    "unused",
    "unused"
};

SwitchExpander SWITCH_EXPANDERS[] = {
  SwitchExpander( 0, exp0Switches ),
  SwitchExpander( 1, exp1Switches )
  // SwitchExpander( 2, exp2Switches ),
  // SwitchExpander( 3, exp3Switches ),
};
