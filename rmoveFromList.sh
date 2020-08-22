start=$(date +%H:%M)
count=0
input="com.csv"
while IFS= read -r line
	do
	let count=count+1
	for file in /root/syngenta/Friday/one/*.csv
		do 
			sed -i "s/${line}//g" "$file"  
			#set -x; echo "$line"
			echo "Count: "$count " on " $file; 
		done
done < "$input"
end=$(date +%H:%M)    
runtime=$(python -c "print(${end} - ${start})")
echo "Runtime was $runtime"
