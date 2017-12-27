TEMPLATE = app
SOURCES += main.cpp
CONFIG += debug_and_release c++14
CONFIG -= qt app_bundle
TARGET = demo
LIBS += -lz -lm -lrt
QMAKE_MAKEFILE = Makefile_$$TARGET
