#include<iostream>
#include<string>

using namespace std;

int main(){
  string s;

  int insertions = 0;
  getline(cin, s);
  int end = s.size()-1;
  int start = 0;
  
  while (start < end){
    if (s[start] == s[end]){
      ++start;
      --end;
      continue;
    }

    if ('x' == s[end]){
      ++insertions;
      --end;
    }
    else if ('x' == s[start]){
      ++insertions;
      ++start;
    }
    else {
      cout<<-1;
      return 0;
    }
  }
  cout<<insertions;
  return 0;
  
}
