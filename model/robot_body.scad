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
	difference(){
		translate([0])
		cube([2.5,15,25]);
		translate([-0.1,7.5,20])
		rotate(90,[0,1,0])
		cylinder(d=2.5, h=2.7);
	}
	difference(){
		translate([67.5,0,0])
		cube([2.5,15,25]);
		translate([67.4,7.5,20])
		rotate(90,[0,1,0])
		cylinder(d=2.5, h=2.7);
	}	
}
