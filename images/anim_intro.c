#include <td_anim.h>

#include <anim_intro/01.c>
#include <anim_intro/02.c>
#include <anim_intro/03.c>
#include <anim_intro/04.c>
#include <anim_intro/05.c>
#include <anim_intro/06.c>
#include <anim_intro/07.c>
#include <anim_intro/08.c>
#include <anim_intro/09.c>
#include <anim_intro/10.c>
#include <anim_intro/11.c>
#include <anim_intro/12.c>
#include <anim_intro/13.c>
#include <anim_intro/14.c>
#include <anim_intro/15.c>
#include <anim_intro/16.c>
#include <anim_intro/17.c>
#include <anim_intro/18.c>
#include <anim_intro/19.c>
#include <anim_intro/20.c>
#include <anim_intro/21.c>
#include <anim_intro/22.c>
#include <anim_intro/23.c>
#include <anim_intro/24.c>
#include <anim_intro/25.c>
#include <anim_intro/26.c>
#include <anim_intro/27.c>
#include <anim_intro/28.c>

#define DEFINE_FRAME(f_raw, f_len) (td_anim_frame_t) { .raw = f_raw, .len = f_len }

td_anim_frame_t anim_intro[] = {
	// DEFINE_FRAME(anim_intro_01_png, anim_intro_01_png_len),
	// DEFINE_FRAME(anim_intro_02_png, anim_intro_02_png_len),
	// DEFINE_FRAME(anim_intro_03_png, anim_intro_03_png_len),
	// DEFINE_FRAME(anim_intro_04_png, anim_intro_04_png_len),
	// DEFINE_FRAME(anim_intro_05_png, anim_intro_05_png_len),
	// DEFINE_FRAME(anim_intro_06_png, anim_intro_06_png_len),
	// DEFINE_FRAME(anim_intro_07_png, anim_intro_07_png_len),
	// DEFINE_FRAME(anim_intro_08_png, anim_intro_08_png_len),
	// DEFINE_FRAME(anim_intro_09_png, anim_intro_09_png_len),
	// DEFINE_FRAME(anim_intro_10_png, anim_intro_10_png_len),
	// DEFINE_FRAME(anim_intro_11_png, anim_intro_11_png_len),
	// DEFINE_FRAME(anim_intro_12_png, anim_intro_12_png_len),
	// DEFINE_FRAME(anim_intro_13_png, anim_intro_13_png_len),
	// DEFINE_FRAME(anim_intro_14_png, anim_intro_14_png_len),
	// DEFINE_FRAME(anim_intro_15_png, anim_intro_15_png_len),
	// DEFINE_FRAME(anim_intro_16_png, anim_intro_16_png_len),
	// DEFINE_FRAME(anim_intro_17_png, anim_intro_17_png_len),
	// DEFINE_FRAME(anim_intro_18_png, anim_intro_18_png_len),
	// DEFINE_FRAME(anim_intro_19_png, anim_intro_19_png_len),
	// DEFINE_FRAME(anim_intro_20_png, anim_intro_20_png_len),
	// DEFINE_FRAME(anim_intro_21_png, anim_intro_21_png_len),
	// DEFINE_FRAME(anim_intro_22_png, anim_intro_22_png_len),
	// DEFINE_FRAME(anim_intro_23_png, anim_intro_23_png_len),
	// DEFINE_FRAME(anim_intro_24_png, anim_intro_24_png_len),
	// DEFINE_FRAME(anim_intro_25_png, anim_intro_25_png_len),
	// DEFINE_FRAME(anim_intro_26_png, anim_intro_26_png_len),
	// DEFINE_FRAME(anim_intro_27_png, anim_intro_27_png_len),
	// DEFINE_FRAME(anim_intro_28_png, anim_intro_28_png_len),
};
size_t anim_intro_len = sizeof(anim_intro) / sizeof(td_anim_frame_t);
