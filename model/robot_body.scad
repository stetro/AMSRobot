union(){
	difference(){
		cube([70,68,2.5]);
		translate([5,10,0])
		cube([60,48,2.5]);
		translate([10,5,0])
		cylinder(d=4, h=2.5);
		translate([60,5,0])
		cylinder(d=4, h=2.5);
		translate([10,63,0])
		cylinder(d=4, h=2.5);
		translate([60,63,0])
		cylinder(d=4, h=2.5);
	}
	
	translate([24,0]){
		cube([20,10,40]);
		translate([10,5,40])
		sphere(d=10);
	}

	difference(){
		translate([0,22.5,0])
		cube([2.5,45,35]);

		translate([0,32.5,0])
		cube([2.5,25,35]);

		translate([-0.1,27.5,30])
		rotate(90,[0,1,0])
		cylinder(d=4, h=2.7);

		translate([-0.1,62.5,30])
		rotate(90,[0,1,0])
		cylinder(d=4, h=2.7);
	}
	difference(){
		translate([67.5,22.5,0])
		cube([2.5,45,35]);

		translate([67.5,32.5,0])
		cube([2.5,25,35]);

		translate([67.4,27.5,30])
		rotate(90,[0,1,0])
		cylinder(d=4, h=2.7);

		translate([67.4,62.5,30])
		rotate(90,[0,1,0])
		cylinder(d=4, h=2.7);
	}
}
