//wheel
d=50;//diameter
hmount=10;//width of inner ring
dmount=5;//diameter of inner ring
spikes=5;
//wheel
difference(){
	union(){
		//outer ring
		difference(){
			cylinder(d=d,h=4);
			translate([0,0,-0.1])
			cylinder(d=(d-4),h=5);
		}
		difference(){
			//spikes
			union(){
				for (i=[0:360/spikes:360]){
					rotate(i,[0,0,1])
					translate([0,-1,0])
					cube([d/2,2,4]);
				}
				//inner ring
				cylinder(d=dmount+6,h=hmount);
			}
			//mount
			translate([0,0,-1])
			cylinder(d=dmount,h=hmount+2);
		}	
	}
	//rubber mount
	translate([0,0,1]){
		difference(){
			cylinder(d=d+1,h=2);
			cylinder(d=d-1,h=2);
		}
	}
}
