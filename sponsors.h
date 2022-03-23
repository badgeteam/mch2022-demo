
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
	// Bosch.
	SPON_BOSCH,
	// Espressif.
	SPON_ESP,
	// Lattice.
	SPON_LATTICE,
	// Raspberry pi.
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
