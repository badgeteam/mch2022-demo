
#ifndef TD_ANIM_H
#define TD_ANIM_H

#include <stdint.h>
#include <stddef.h>

typedef struct td_anim_frame {
    const char *raw;
    size_t      len;
} td_anim_frame_t;

extern td_anim_frame_t anim_intro[];
extern size_t          anim_intro_len;

#endif //TD_ANIM_H
