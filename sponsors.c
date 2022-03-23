
#include "sponsors.h"

// Handy definition.
#define DEFINE_SPONSOR(logo_id, the_text) {\
    .text     = the_text,\
    .logo     = logo_id##_png,\
    .logo_len = logo_id##_png_len\
}

// Temporary sponsor placeholder of.
#include "images/temp_logo.c"

// Bosch logo.
#include "images/logo/bosch.c"

// The array.
sponsor_t sponsors_arr[] = {
    // Temporary sponsor placeholder of.
    DEFINE_SPONSOR(temp_logo, "Placeholder"),
    // Bosch (need logo image).
    DEFINE_SPONSOR(logo_bosch, "Bosch:\nBNO-055\nMBE-680"),
    // Espressif (need logo image).
    DEFINE_SPONSOR(temp_logo, "Espressif:\nESP32 MCU"),
    // Lattice (need logo image).
    DEFINE_SPONSOR(temp_logo, "Lattice:\nICE40 UP5K"),
    // Raspberry pi (need logo image).
    DEFINE_SPONSOR(temp_logo, "Raspberry pi:\nRP2040 coprocessor"),
};
