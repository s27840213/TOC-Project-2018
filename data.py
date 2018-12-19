class MembData():
    def __init__(self,name,gender,grade,place,intro):
        self.name=name
        self.gender=gender
        self.grade=grade
        self.place=place
        self.intro=intro

yochen = MembData('張祐禎','男','109級大三','大砲','大帥哥')
tzu = MembData('歐子毓','男','109級大三','自由球員','醜男')
smallhow = MembData('朱浩澤','男','109級大三','舉球員','醜男')
peihsuan = MembData('洪培軒','男','109級大三','大砲','醜男')
# yochen = MembData('張祐禎','大三','大砲','醜男')
# yochen = MembData('張祐禎','大三','大砲','醜男')
# yochen = MembData('張祐禎','大三','大砲','醜男')
# yochen = MembData('張祐禎','大三','大砲','醜男')
# yochen = MembData('張祐禎','大三','大砲','醜男')

membDict = {'張祐禎':yochen,'歐子毓':tzu,'朱浩澤':smallhow,'洪培軒':peihsuan}
