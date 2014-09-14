#Simplified BSD License
#
#Copyright (c) 2014, Michael Strecke
#MStrecke@gmx.de
#All rights reserved.
#
#Redistribution and use in source and binary forms, with or without
#modification, are permitted provided that the following conditions are met:
#
#1. Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
#2. Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
#
#THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
#ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
#WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
#DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
#ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
#(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
#LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
#ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
#(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
#SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#################################################################

bl_info = {
    "name": "Random Cycles Seed",
    "author": "karamike",
    "version": (1, 0),
    "blender": (2, 71, 0),
    "location": "Rendertab -> Sampling Panel",
    "description": "Choose random seed for Cycles render",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Render"}

import bpy
from bpy.app.handlers import persistent
from mathutils import noise
from bpy.props import BoolProperty

@persistent
def set_random_seed(scene):
    if scene.cycles_random_seed:
        bpy.context.scene.cycles.seed = noise.random() * 10000
        print("New cycles seed", bpy.context.scene.cycles.seed)

def random_seed_UI(self, context):
    layout = self.layout
    split = layout.split(percentage=1.0, align=True)
    row = split.row()
    row.prop(context.scene, 'cycles_random_seed', text='Random Seed', toggle=False)

def register():
    bpy.types.Scene.cycles_random_seed = BoolProperty(
                    name='random seed',
                    default=False,
                    description='Choose random Cycles seed value before rendering')
    bpy.app.handlers.render_pre.append(set_random_seed)
    bpy.types.CyclesRender_PT_sampling.append(random_seed_UI)

def unregister():
    del(bpy.types.Scene.cycles_random_seed)
    bpy.app.handlers.render_post.remove(set_random_seed)
    bpy.types.CyclesRender_PT_sampling.remove(random_seed_UI)

if __name__ == "__main__":
    register()


