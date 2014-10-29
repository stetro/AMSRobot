
difference(){
	union(){
		sphere(d=35);
		translate([-20,-20,10])
		cube([40,40,8]);
	}
	sphere(d=33);
	translate([0,0,-5])
	cube([1,20,15]);
	translate([-20,-20,-25])
	cube([40,40,20]);
}
