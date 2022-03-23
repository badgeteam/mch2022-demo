
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
// Espressif logo.
#include "images/logo/espressif.c"
// Lattice logo.
#include "images/logo/lattice.c"
// Raspberry pi logo.
#include "images/logo/raspberry_pi.c"

// The array.
sponsor_t sponsors_arr[] = {
	// Temporary sponsor placeholder of.
	DEFINE_SPONSOR(temp_logo,         "Placeholder"),
	// Bosch.
	DEFINE_SPONSOR(logo_bosch,        "Bosch:\nBNO-055\nMBE-680"),
	// Espressif.
	DEFINE_SPONSOR(logo_espressif,    "Espressif:\nESP32 MCU"),
	// Lattice.
	DEFINE_SPONSOR(logo_lattice,      "Lattice:\nICE40 UP5K"),
	// Raspberry pi.
	DEFINE_SPONSOR(logo_raspberry_pi, "Raspberry pi:\nRP2040\ncoprocessor"),
};
