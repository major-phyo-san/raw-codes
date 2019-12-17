void misbehave(){
try{
dynamic foo = true;
print(foo++);
}catch(e){
print('misbehave() partially handled ${e.runtimeType}.');
rethrow;
}
}

void main(){
try{
misbehave();
}
catch(e){
print('main() finished handling ${e.runtimeType}.');
}
}