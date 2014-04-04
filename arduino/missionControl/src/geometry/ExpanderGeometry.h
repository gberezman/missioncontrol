#ifndef EXPANDER_GEOMETRY_H
#define EXPANDER_GEOMETRY_H

// index of switch corresponds to I/O pin of I/O Expander

char* exp0Switches[16] = {
  // CONTROL
  "DockingProbe",
  "GlycolPump",
  "SCEPower",
  "WasteDump",
  "CabinFan",
  "H2OFlow",
  "IntLights",
  "SuitComp",

  // ABORT
  "ArmAbort",
  "Abort",

  "unused",
  "unused",
  "unused",
  "unused",
  "unused",
  "unused"
};

char* exp1Switches[16] = {
  // BOOSTER
  "SPS",
  "TEI",
  "TLI",
  "S-IC",
  "S-II",
  "S-iVB",
  "M-I",
  "M-II",
  "M-III"

  // C&WS
  "Power",
  "Mode",
  "Lamp",
  "Ack",

  // CAPCOM
  "PTT",

  "unused",
  "unused"
};

char* exp2Switches[16] = {
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

char* exp3Switches[16] = {
  // CRYOGENICS
  "O2Fan",
  "H2Fan",
  "Pumps",
  "Heat",

  // PYROTECHNICS
  "MainDeploy",
  "CSM/LVDeploy",
  "SM/CMDeploy",
  "DrogueDeploy",
  "CanardDeploy",
  "ApexCoverJettsn",
  "LesMotorFire",

  "unused",
  "unused",
  "unused",
  "unused",
  "unused"
};

#endif