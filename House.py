import arcade
my_window = arcade.open_window(800, 800, "House")
arcade.set_background_color(arcade.color.LIGHT_BLUE)
arcade.start_render()

arcade.draw_lrtb_rectangle_filled(275,350,675,550, arcade.color.BURGUNDY) #Chimney
arcade.draw_lrtb_rectangle_filled(0,800,200,0, arcade.color.ARMY_GREEN) #Grass
arcade.draw_lrtb_rectangle_filled(200,600,475,75, arcade.color_from_hex_string("#e0c294")) #House block
arcade.draw_triangle_filled(400,700,700,475,100,475, arcade.color.COOL_BLACK) #Roof
arcade.draw_xywh_rectangle_filled(250,250,100,100, arcade.color.WHITE) #Window left
arcade.draw_xywh_rectangle_filled(450,250,100,100, arcade.color.WHITE) #Window right
arcade.draw_lrtb_rectangle_filled(350,450,220,75, arcade.color.SKOBELOFF) #Door
arcade.draw_circle_filled(360,145,6, arcade.color.GOLD) #Knob

arcade.finish_render()
arcade.run()