import turtle as tu
 
 
class allu_arjun:
    def __init__(self):
        
        self.border = [(163, 104), (572, 105), (573, 619), (164, 618)]
        self.dress = [(164, 574), (166, 574), (176, 562), (174, 562), (178, 551), (191, 522), (195, 513), (203, 496), (211, 479), (215, 470), (223, 455), (229, 443), (235, 434), (236, 427), (240, 420), (246, 412), (252, 408), (254, 404), (264, 389), (274, 371), (270, 371), (284, 353), (287, 348), (292, 341), (298, 336), (299, 330), (303, 326), (307, 322), (309, 307), (313, 308), (313, 302), (316, 295), (318, 290), (321, 282), (324, 274), (327, 267), (329, 266), (329, 262), (336, 259), (345, 254), (356, 247), (365, 243), (367, 240), (371, 233), (368, 231), (366, 228), (364, 223), (362, 217), (361, 211), (360, 205), (359, 200), (360, 193), (358, 185), (358, 177), (355, 170), (353, 165), (354, 160), (354, 155), (355, 151), (356, 147), (358, 151), (360, 144), (364, 141), (368, 138), (373, 135), (378, 134), (383, 134), (390, 135), (401, 136), (405, 138), (411, 141), (416, 143), (420, 147), (424, 151), (426, 156), (428, 162), (429, 171), (430, 177), (431, 184), (430, 189), (432, 192), (430, 193), (432, 195), (430, 200), (430, 205), (434, 208), (431, 210), (434, 215), (432, 219), (430, 222), (430, 228), (436, 231), (448, 233), (456, 234), (460, 238), (467, 238), (474, 241), (479, 245), (481, 249), (493, 258), (500, 260), (501, 266), (505, 269), (505, 274), (508, 276), (511, 279), (516, 279), (517, 284), (521, 288), (526, 293), (530, 296), (531, 300), (536, 307), (540, 314), (545, 318), (547, 322), (547, 327), (548, 333), (547, 338), (544, 342), (541, 346), (538, 349), (536, 352), (532, 356), (539, 360), (540, 367), (534, 369), (527, 364), (525, 364), (522, 367), (517, 371), (512, 376), (506, 380), (500, 384), (492, 389), (484, 393), (480, 396), (481, 405), (480, 416), (483, 425), (483, 434), (482, 440), (479, 446), (476, 451), (468, 455), (459, 458), (452, 459), (443, 461), (438, 462), (436, 462), (434, 463), (433, 469), (433, 475), (429, 488), (425, 496), (420, 504), (414, 516), (410, 526), (406, 539), (403, 548), (400, 554), (399, 560), (397, 565), (397, 568), (400, 574), (391, 579), (391, 582), (394, 585), (385, 614), (383, 612), (354, 618), (355, 614), (353, 610), (355, 605), (357, 601), (358, 596), (360, 591), (363, 580), (366, 573), (366, 567), (369, 564), (368, 561), (370, 551), (373, 546), (380, 530), (381, 518), (382, 507), (381, 492), (383, 478), (384, 469), (387, 455), (389, 448), (388, 435), (385, 430), (387, 442), (382, 452), (371, 454), (359, 455), (339, 459), (321, 462), (308, 466), (294, 469), (289, 467), (283, 465), (277, 467), (274, 470), (273, 475), (269, 481), (267, 488), (261, 500), (256, 508), (251, 517), (242, 533), (235, 547), (229, 556), (224, 564), (217, 571), (211, 578), (209, 585), (210, 592), (211, 598), (212, 607), (211, 610), (211, 619), (165, 619)]
        self.bg = [(164, 277), (171, 277), (179, 279), (204, 277), (231, 276), (252, 276), (272, 276), (290, 271), (300, 271), (314, 280), (316, 287), (283, 466), (283, 479), (282, 492), (281, 500), (281, 510), (279, 518), (277, 526), (271, 527), (260, 530), (244, 532), (244, 536), (244, 543), (247, 549), (252, 549), (259, 553), (269, 552), (270, 530), (183, 540), (164, 543), (164, 543), (164, 437), (164, 342), (165, 278)]
        self.line = [(358, 180), (362, 180), (366, 183), (362, 183), (359, 183), (358, 184), (358, 182), (-1, -1), (377, 180), (382, 180), (388, 180), (394, 183), (388, 182), (385, 182), (378, 183), (377, 181),]
        self.eyeb = [(361, 189), (363, 190), (364, 190), (365, 190), (366, 189), (366, 186), (-1, -1), (383, 186), (383, 188), (384, 189), (386, 189), (389, 188), (-1, -1)]
        self.nose1 = [(371, 205), (370, 204), (372, 203), (374, 202), (376, 204), (374, 204), (-1, -1)]
        self.beard =[(367, 210), (371, 210), (376, 211), (379, 212), (375, 213), (372, 213), (368, 213), (365, 212), (-1, -1), (377, 218), (374, 221), (371, 221), (368, 220), (366, 218), (368, 217), (376, 217), (378, 216), (377, 214), (367, 214), (365, 215), (365, 217), (365, 220), (366, 223), (369, 227), (373, 227), (376, 225), (378, 225), (379, 222), (383, 219), (383, 217), (380, 215), (-1, -1)]
        self.skin = [(377, 233), (377, 238), (377, 243), (379, 249), (379, 254), (382, 257), (384, 259), (386, 263), (393, 269), (397, 276), (400, 271), (403, 265), (407, 258), (412, 252), (415, 248), (416, 240), (417, 235), (416, 232), (414, 227), (415, 220), (414, 214), (414, 210), (414, 208), (412, 208), (416, 208), (418, 206), (420, 204), (421, 200), (421, 203), (422, 201), (423, 198), (423, 194), (423, 191), (422, 188), (420, 187), (417, 189), (413, 192), (411, 196), (408, 197), (407, 191), (405, 187), (402, 184), (399, 182), (396, 178), (398, 172), (397, 170), (395, 168), (392, 167), (389, 166), (389, 170), (386, 167), (385, 171), (378, 171), (381, 169), (382, 164), (379, 167), (378, 170), (375, 168), (374, 165), (373, 168), (370, 168), (371, 166), (372, 164), (369, 164), (366, 164), (364, 166), (362, 170), (362, 174), (358, 178), (357, 182), (358, 185), (359, 189), (358, 195), (358, 199), (359, 203), (360, 208), (361, 213), (362, 220), (364, 225), (366, 229), (371, 232), (377, 233), (383, 232), (390, 232), (396, 231), (401, 227), (404, 223), (406, 219), (408, 216), (410, 213), (413, 211), (-1, -1), (498, 342), (501, 340), (506, 341), (512, 343), (517, 347), (523, 352), (526, 357), (524, 362), (520, 366), (512, 373), (507, 377), (502, 381), (495, 384), (490, 388), (483, 391), (477, 393), (477, 387), (475, 384), (476, 380), (472, 375), (469, 375), (473, 373), (477, 370), (482, 365), (487, 360), (491, 355), (495, 348), (498, 343), (-1, -1), (458, 379), (461, 385), (465, 391), (467, 398), (467, 402), (463, 404), (458, 403), (451, 398), (444, 393), (441, 391), (435, 388), (425, 388), (416, 389), (413, 389), (416, 385), (419, 382), (424, 379), (430, 375), (435, 373), (441, 374), (447, 377), (452, 379), (457, 381), (-1, -1), (273, 370), (277, 368), (283, 367), (291, 371), (298, 378), (301, 384), (301, 390), (299, 394), (296, 397), (289, 401), (283, 404), (277, 409), (275, 410), (276, 417), (276, 426), (279, 433), (278, 436), (275, 436), (272, 434), (270, 431), (270, 427), (269, 420), (268, 416), (267, 413), (264, 414), (261, 419), (261, 426), (262, 432), (264, 429), (267, 426), (261, 432), (263, 436), (265, 440), (268, 444), (270, 450), (269, 452), (273, 454), (274, 458), (271, 460), (269, 459), (268, 458), (267, 459), (265, 460), (262, 459), (258, 459), (253, 456), (251, 453), (249, 448), (247, 441), (245, 432), (245, 429), (245, 424), (249, 418), (253, 412), (253, 407), (253, 404), (256, 400), (259, 396), (264, 387), (267, 382), (270, 376), (273, 372), (273, 370), (276, 369), (281, 367), (287, 368), (294, 373), (301, 382), (301, 390), (299, 395), (296, 397), (289, 401), (283, 404), (277, 408), (276, 410), (272, 406), (271, 404), (271, 399), (270, 396), (-1, -1), (177, 564), (180, 563), (185, 565), (191, 569), (197, 572), (201, 575), (202, 580), (201, 584), (198, 588), (194, 590), (188, 591), (181, 588), (178, 586), (175, 584), (172, 582), (170, 578), (167, 575), (169, 573), (172, 569), (175, 566), (178, 562), (182, 563), (185, 565), (-1, -1), (365, 577), (367, 575), (370, 573), (374, 574), (374, 571), (372, 569), (371, 566), (370, 563), (369, 565), (367, 568), (366, 572), (365, 574), (-1, -1), (269, 428), (268, 421), (268, 417), (266, 414), (263, 415), (262, 419), (261, 427), (263, 429), (266, 427), (269, 428), (-1, -1), (310, 394), (327, 391), (345, 391), (356, 389), (358, 380), (359, 367), (355, 350), (348, 329), (347, 334), (345, 336), (342, 343), (337, 350), (333, 355), (329, 362), (329, 366), (324, 374), (319, 379), (317, 383), (312, 392), (311, 394), (-1, -1), (481, 317), (488, 320), (494, 328), (498, 334), (495, 340), (495, 343), (491, 352), (485, 359), (477, 367), (477, 346), (481, 317), (-1, -1)]
        self.face = [(360, 190), (362, 191), (364, 192), (366, 191), (368, 190), (369, 189), (369, 188), (368, 187), (367, 186), (364, 186), (361, 186), (360, 187), (-1, -1), (379, 187), (380, 189), (382, 190), (384, 190), (387, 190), (390, 190), (393, 188), (390, 186), (388, 184), (385, 184), (382, 184), (380, 186), (-1, -1), (362, 214), (363, 210), (365, 207), (366, 206), (370, 206), (374, 206), (377, 206), (380, 207), (383, 209), (385, 213), (385, 217), (386, 222), (385, 228), (383, 230), (378, 232), (373, 232), (368, 230), (365, 224), (363, 218), (362, 214), (-1, -1)]
        self.nose = [(374, 189), (374, 194), (373, 198), (376, 200), (378, 202), (378, 205), (376, 205), (374, 205), (371, 205),
(369, 205), (367, 204), (365, 202), (367, 200), (369, 198)]
        self.eye = [(359, 187), (361, 186), (364, 186), (367, 187), (-1, -1), (360, 190), (363, 191), (366, 191), (368, 190), (-1, -1), (380, 188), (381, 186), (384, 186), (388, 187), (390, 188), (-1, -1), (382, 190), (385, 190), (389, 189), (-1, -1), (360, 192), (364, 193), (368, 192), (-1, -1), (380, 191), (385, 192), (390, 192), (-1, -1), (370, 191), (367, 197), (364, 201), (365, 203), (367, 204), (369, 205), (371, 205), (373, 204), (376, 204), (378, 203), (379, 201), (378, 200), (375, 198), (374, 197), (-1, -1)]
        self.bgthings = [(441, 464), (466, 465), (493, 466), (518, 466), (547, 461), (562, 454), (557, 447), (555, 446), (549, 442), (543, 440), (530, 435), (510, 433), (489, 432), (483, 432), (-1, -1), (562, 454), (564, 461), (565, 469), (566, 475), (566, 486), (565, 520), (565, 533), (564, 542), (563, 553), (562, 568), (559, 577), (552, 584), (546, 586), (533, 589), (522, 592), (503, 596), (426, 599), (411, 598), (357, 593), (340, 588), (314, 580), (311, 574), (308, 565), (308, 550), (308, 535), (308, 516), (308, 478), (308, 467), (321, 464), (339, 460), (350, 457), (363, 458), (371, 460), (383, 459), (385, 455), (352, 457), (383, 460), (-1, -1), (271, 529), (277, 527), (284, 469), (291, 471), (308, 467), (308, 479), (308, 551), (307, 557), (298, 558), (286, 561), (278, 563), (258, 565), (248, 567), (216, 573), (226, 563), (232, 554), (244, 532), (244, 547), (252, 551), (258, 553), (269, 553), (270, 530), (-1, -1), (183, 541), (167, 544), (165, 571), (167, 572), (174, 564), (175, 556), (176, 552), (179, 549), (181, 540), (-1, -1), (211, 596), (228, 599), (252, 603), (275, 607), (295, 611), (313, 613), (323, 613), (343, 618), (211, 618), (211, 610), (211, 596)]
        self.lines = [(318, 290), (325, 298), (330, 302), (-1, -1), (329, 289), (328, 294), (333, 299), (-1, -1), (312, 306), (309, 307), (312, 310), (318, 313), (325, 316), (-1, -1), (315, 298), (317, 300), (319, 303), (323, 306), (328, 309), (-1, -1), (317, 296), (320, 299), (324, 303), (328, 306), (-1, -1), (325, 316), (331, 320), (338, 324), (-1, -1), (291, 345), (295, 341), (299, 340), (305, 343), (314, 348), (319, 355), (-1, -1), (298, 344), (301, 348), (308, 353), (-1, -1), (294, 347), (300, 350), (305, 354), (311, 358), (314, 362), (316, 365), (320, 370), (-1, -1), (288, 350), (293, 351), (301, 356), (308, 363), (313, 368), (317, 374), (-1, -1), (275, 411), (273, 407), (271, 405), (271, 401), (270, 396), (-1, -1), (258, 441), (260, 444), (262, 446), (-1, -1), (253, 426), (254, 432), (-1, -1), (253, 451), (258, 455), (-1, -1), (242, 439), (253, 477), (251, 455), (256, 477), (-1, -1), (237, 443), (238, 454), (243, 479), (-1, -1), (214, 506), (215, 519), (215, 526), (212, 537), (207, 549), (199, 558), (201, 562), (209, 557), (-1, -1), (181, 552), (188, 554), (196, 558), (208, 566), (213, 572), (-1, -1), (211, 607), (209, 611), (206, 613), (200, 614), (164, 615), (-1, -1), (202, 582), (191, 584), (-1, -1), (263, 469), (249, 497), (226, 534), (218, 545), (-1, -1), (284, 439), (308, 433), (330, 431), (365, 425), (385, 424), (-1, -1), (358, 390), (365, 387), (374, 387), (384, 386), (386, 384), (389, 383), (395, 383), (401, 384), (412, 385), (-1, -1), (387, 398), (386, 386), (-1, -1), (311, 430), (294, 414), (-1, -1), (315, 429), (298, 412), (323, 429), (304, 409), (-1, -1), (328, 427), (309, 408), (-1, -1), (337, 427), (313, 408), (-1, -1), (344, 424), (324, 405), (-1, -1), (327, 414), (318, 406), (-1, -1), (358, 420), (330, 400), (-1, -1), (368, 421), (344, 405), (-1, -1), (369, 418), (347, 403), (335, 398), (-1, -1), (348, 404), (338, 396), (-1, -1), (373, 417), (360, 407), (-1, -1), (373, 413), (353, 398), (-1, -1), (378, 407), (368, 402), (356, 395), (-1, -1), (381, 405), (363, 394), (-1, -1), (368, 392), (378, 392), (385, 392), (-1, -1), (372, 425), (366, 435), (-1, -1), (372, 425), (369, 438), (-1, -1), (280, 439), (285, 451), (291, 461), (-1, -1), (436, 436), (430, 429), (421, 417), (-1, -1), (440, 433), (431, 407), (-1, -1), (388, 437), (396, 427), (-1, -1), (387, 432), (398, 411), (-1, -1), (386, 432), (387, 426), (389, 417), (394, 407), (-1, -1), (481, 386), (490, 381), (502, 370), (511, 361), (523, 352), (-1, -1), (440, 384), (434, 381), (427, 381), (-1, -1), (331, 263), (331, 278), (331, 286), (334, 298), (339, 307), (342, 316), (348, 326), (-1, -1), (378, 260), (384, 271), (387, 286), (-1, -1), (374, 261), (377, 279), (380, 291), (388, 299), (-1, -1), (358, 262), (356, 273), (359, 279), (-1, -1), (364, 261), (363, 265), (361, 272), (360, 279), (-1, -1), (467, 247), (458, 261), (456, 271), (448, 288), (-1, -1), (474, 243), (468, 248), (465, 256), (465, 265), (465, 272), (464, 282), (465, 297), (473, 310), (480, 315), (476, 307), (472, 300), (472, 295), (476, 289), (480, 285), (484, 279), (488, 273), (491, 270), (486, 284), (492, 275), (497, 266), (500, 263), (-1, -1), (493, 262), (483, 265), (479, 273), (471, 289), (478, 283), (-1, -1), (303, 329), (318, 331), (330, 342), (341, 344), (-1, -1), (527, 336), (535, 344), (533, 334), (533, 328), (526, 323), (519, 321), (507, 323), (512, 320), (521, 318), (531, 318), (538, 321), (-1, -1), (545, 324), (541, 318), (536, 316), (527, 315), (522, 315), (516, 316), (510, 317), (502, 322), (499, 330), (-1, -1), (497, 326), (497, 318), (499, 309), (501, 303), (504, 300), (515, 301), (512, 311), (518, 306), (528, 299), (523, 296), (512, 296), (509, 296), (520, 288), (512, 289), (502, 294), (501, 289), (513, 283), (-1, -1), (510, 280), (497, 289), (506, 277), (-1, -1), (502, 271), (488, 292), (484, 300), (479, 305), (-1, -1), (431, 250), (432, 262), (430, 275), (435, 268), (441, 258), (444, 273), (448, 284), (-1, -1), (415, 307), (415, 296), (415, 308), (416, 323), (427, 325), (442, 326), (447, 323), (447, 294), (437, 294), (422, 295), (415, 296), (-1, -1), (402, 272), (400, 280), (400, 288), (400, 297), (399, 309), (399, 317), (400, 325), (402, 332), (402, 344), (403, 355), (402, 364), (402, 381), (-1, -1), (356, 316), (366, 309), (376, 306), (386, 312), (-1, -1), (365, 243), (361, 251), (359, 263), (363, 256), (368, 256), (-1, -1), (436, 248), (420, 247), (436, 249), (428, 228), (434, 236), (449, 241), (461, 243), (-1, -1),(400, 568), (396, 578), (387, 578), (378, 575), (372, 566), (368, 560), (371, 549), (372, 557), (378, 563),
(385, 567), (393, 568), (401, 568), (-1, -1), (369, 563), (375, 572), (365, 578), (367, 571), (367, 568), (369, 564), (-1, -1), (372, 578), (372, 583), (373, 586),
(375, 590), (-1, -1), (357, 604), (368, 602), (384, 596), (387, 602), (-1, -1), (391, 549), (387, 562), (384, 567), (-1, -1), (426, 439), (419, 480), (391, 550), (-1, -1), (440, 461), (455, 464), (475, 465), (496, 466), (520, 464), (538, 462), (554, 460), (558, 457), (562, 454), (562, 451), (560, 449), (555, 446), (-1, -1), (520, 465), (519, 484), (510, 593), (510, 595), (-1, -1), (438, 441), (440, 448), (437, 457), (435, 463), (-1, -1),]
        self.pen = tu.Turtle()
        self.pen.hideturtle()
        self.pen.speed(0)
        self.x_offset = 300
        self.y_offset = 300
 
 
    def go(self, x, y):
        self.pen.penup()
        self.pen.goto(x-self.x_offset,(y*-1)+self.y_offset)
        self.pen.pendown()  
 
 
    def paint(self,coord,co=(0,0,0),pco=('white')):
        self.pen.color(pco)
        t_x,t_y = coord[0]
        self.go(t_x,t_y)
        self.pen.fillcolor(co)
        self.pen.begin_fill()
        t = 0
        for i in coord[1:]:
            print(i)
            x,y = i
            if t:
                self.go(x,y)
                t = 0
                self.pen.begin_fill()
                continue
            if x == -1 and y == -1:
                t = 1
                self.pen.end_fill()
                continue
            else:
                self.pen.goto(x-self.x_offset,(y*-1)+self.y_offset) 
        self.pen.end_fill()
 
 
    def draw_fn(self,coord,mode = 1,co = (0,0,0),thickness = 1,pco = ('white' )):
        co = (co[0]/255,co[1]/255,co[2]/255)
        
        self.pen.color(pco)
        
        #self.pen.pencolor(pco)
 
        if mode:
            self.pen.width(thickness)
            t_x,t_y = coord[0]
            self.go(t_x,t_y)
            t = 0
            for i in coord[1:]:
                print(i)
                x,y = i
                if t:
                    self.go(x,y)
                    t = 0
                    continue
                if x == -1 and y == -1:
                    t = 1
                    continue
                else:
                    self.pen.goto(x-self.x_offset,(y*-1)+self.y_offset)
        else:
            
            self.paint(coord=coord,pco = pco,co = co)
 
 
    
    def draw(self,retain=True):
        self.draw_fn(self.border,mode = 0)
        self.draw_fn(self.bg,pco=('red'),mode = 0)
        self.draw_fn(self.bgthings,co=(255,255,255),pco=('red'),mode = 0)
        self.draw_fn(self.dress,co=(0,0,0),pco=('red'),mode = 0)
        self.draw_fn(self.skin,co=(255,255,255),pco=('red'),mode = 0)
        self.draw_fn(self.line,pco=('black'),mode=0,thickness=2)
        self.draw_fn(self.face,pco=('black'),mode=0)
        self.draw_fn(self.beard,pco=('white'),mode=0,co=(255,255,255))
        self.draw_fn(self.eyeb,pco=('white'),mode=0,thickness=3)
        self.draw_fn(self.nose,pco=('black'),mode=0)
        self.draw_fn(self.nose1,pco=('white'),mode=0,co=(255,255,255))
        self.draw_fn(self.lines,pco=('red'),mode=1)
        if retain:
            tu.done()
pen = allu_arjun()

pen.draw()