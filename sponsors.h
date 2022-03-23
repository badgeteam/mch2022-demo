
#ifndef SPONSORS_H
#define SPONSORS_H

#ifdef __cplusplus
extern "C" {
#endif //__cplusplus

#include <stdint.h>
#include <stddef.h>

enum sponsors {
	// Temporary sponsor placeholder of.
	SPON_TEMP,
	// Bosch (need logo image).
	SPON_BOSCH,
	// Espressif (need logo image).
	SPON_ESP,
	// Lattice (need logo image).
	SPON_LATTICE,
	// Raspberry pi (need logo image).
	SPON_RASB_PI,
};

struct sponsor {
	// Sponsor text, optional.
	char  *text;
	// Sponsor logo in PNG form.
	void  *logo;
	// Length of the raw PNG.
	size_t logo_len;
};

typedef enum sponsors sponsors_t;
typedef struct sponsor sponsor_t;

extern sponsor_t sponsors_arr[];

#ifdef __cplusplus
}
#endif //__cplusplus

#endif //SPONSORS_H
