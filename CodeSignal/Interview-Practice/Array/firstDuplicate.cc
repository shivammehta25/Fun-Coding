#include<iostream>
#include<vector>
#include<cstdlib>

using namespace std;


int firstDuplicate(vector<int> a) {
  for(int i=0;i<a.size();i++){
    a[abs(a[i]) - 1] *= -1;
    if (a[abs(a[i]) - 1]  > 0){
      return abs(a[i]);
    }
  }
  return -1;
}


int main(){
  int n;
  cin>>n;
  vector<int> a;
  for(int i=0; i<n ; i++){
    int input;
    cin>>input;
    a.push_back(input);
  }
  cout<<firstDuplicate(a);

}
