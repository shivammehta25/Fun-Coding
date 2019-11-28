#include<iostream>
#include<string>
#include<cmath>
#include<map>


using namespace std;

int main(){
  string c;
  getline(cin, c);
  map<char, int> dict;
  for(int i = 0; i < c.size(); ++i){
    if (dict.find(c[i]) != dict.end()){
      dict[c[i]] = -1;
    }
    else{
      dict[c[i]] = i;
    }
  }
  double res = pow(10,5) + 1;  
  map<char, int>::iterator it;
  
  for( it = dict.begin(); it != dict.end(); it++){
    if (it->second >= 0){
      if (res > it->second){
	res = it->second;
      }
    }
  }

  if (res > pow(10, 5)){
    cout<<'_';
  }
  else{
    cout<<c[res];
  }
  

  
  
}
