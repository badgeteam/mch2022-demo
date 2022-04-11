
#ifndef TD_ANIM_H
#define TD_ANIM_H

#include <stdint.h>
#include <stddef.h>

typedef struct {
    const int     x;
    const int     y;
    const char   *raw;
    const size_t  len;
} td_anim_part_t;

typedef struct {
    const td_anim_part_t *parts;
    const size_t          len;
} td_anim_frame_t;

#define td_anim_def_part(_x, _y, arr, _len) { .x=(_x), .y=(_y), .raw=(arr), .len=(_len) }
#define td_anim_def_frame(arr, _len) { .parts=(arr), .len=(_len) }

extern const td_anim_frame_t td_anim_frames[];
extern const size_t          td_anim_frames_len;

#endif //TD_ANIM_H
