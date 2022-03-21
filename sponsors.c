
#include "sponsors.h"

// Handy definition.
#define DEFINE_SPONSOR(logo_id, the_text) {\
    .text     = the_text,\
    .logo     = logo_id##_logo_png,\
    .logo_len = logo_id##_logo_png_len\
}

// Temporary sponsor placeholder of.
#include "images/temp_logo.c"

// The array.
sponsor_t sponsors_arr[] = {
    // Temporary sponsor placeholder of.
    DEFINE_SPONSOR(temp, "Placeholder"),
    // Bosch (need logo image).
    DEFINE_SPONSOR(temp, "Bosch:\nBNO-055\nMBE-680"),
    // Espressif (need logo image).
    DEFINE_SPONSOR(temp, "Espressif:\nESP32 MCU"),
    // Lattice (need logo image).
    DEFINE_SPONSOR(temp, "Lattice:\nICE40 UP5K"),
    // Raspberry pi (need logo image).
    DEFINE_SPONSOR(temp, "Raspberry pi:\nRP2040 coprocessor"),
};
