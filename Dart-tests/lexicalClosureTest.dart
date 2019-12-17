Function makeAdder(num addBy){
	//print(addBy);
	return (num i) {
		return addBy + i;
	};	
}

void main(){
	var add2 = makeAdder(2);
	var add4 = makeAdder(4);
	print(add2(3));
	print(add4(3));
}