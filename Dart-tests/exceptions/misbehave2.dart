void misbehave(){
try{
dynamic foo = true;
print(foo++);
}catch(e){
print('misbehave() partially handled ${e.runtimeType}.');

}
}

void main(){

misbehave();

}