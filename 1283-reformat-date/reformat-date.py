class Solution:
    def reformatDate(self, date: str) -> str:
        month = {"Jan":"01", "Feb":"02", "Mar":"03", "Apr":"04", "May":"05", "Jun":"06", "Jul":"07", 
        "Aug":"08", "Sep":"09", "Oct":"10", "Nov":"11", "Dec":"12"}
        date = date.split(" ")
        # date=["20th"," Oct"," 2052"]
        str_res = ""
        if len(date[0])==3:
            date[0]="0"+date[0][0]
        elif len(date[0])==4:
            date[0]=date[0][0]+date[0][1]
        str_res+=date[2]+"-"+month[date[1]]+"-"+date[0]
        return str_res
        