#using blenderS
import bpyS
import bmesh
obj=bpy.data.objects["Cube"]
obj.select_set(True)
i = 0
for mat_slot in obj.material_slots:
    #enter edit mode
    bpy.ops.object.mode_set(mode="EDIT")
    #deselect all
    bpy.ops.mesh.select_all(action='DESELECT')
    #choose the active slot based on the loop number
    bpy.context.object.active_material_index = i
    #select the faces of the active slot
    bpy.ops.object.material_slot_select()
    #make a bmesh from the mesh
    me = bpy.context.object.data
    bm = bmesh.from_edit_mesh(me)
    #list to populate with lengths
    edge_lengths = []
    #if edge is selected, get its length
    for e in bm.edges:
        if e.select:
            edge_lengths.append(e.calc_length())
    print(edge_lengths)
    i=i+1
bpy.ops.object.mode_set(mode="OBJECT")