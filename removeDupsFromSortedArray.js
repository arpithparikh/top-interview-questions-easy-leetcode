
//Remove Dips
var removeDuplicates = function(nums) {
    
    //remove dups
    
    let start = 0;
    let end = 1;
    
   while(end < nums.length && start < nums.length-1){
       console.log("start:",start);
       console.log("end:",end);
       console.log(nums);
       if(nums[start] == nums[end]){
           console.log("#### removed: ####",nums[end])
           nums.splice(end,1);
         
       }else{
           start++;
           end++
       }   
   }

    console.log("****** output *******")
    console.log(nums);
    return nums.length;
    
    
};


console.log(removeDuplicates([0,0,1,1]));
console.log(removeDuplicates([0,0,1,1,1,2,2,2,2,2,3,3,3,3,3,4,4,4,4,4,4]));
console.log(removeDuplicates([0,0,1,1,1,2,2,3,3,4]));