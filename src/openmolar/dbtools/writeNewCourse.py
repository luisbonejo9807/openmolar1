# -*- coding: utf-8 -*-
# Copyright (c) 2009 Neil Wallace. All rights reserved.
# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. See the GNU General Public License for
# more details.

import MySQLdb,sys
from openmolar.connect import connect
from openmolar.settings import localsettings
from openmolar.dbtools import patient_class

def write(sno,dnt,accd):
    print "new course %d %s %d"%(sno,accd,dnt)
    query=""
    for att in patient_class.currtrtmtTableAtts:
        value=""
        if att in patient_class.dateFields:
            if att=="accd":
                print "new course date=",accd
                query+='%s="%s" ,'%(att,accd)
        elif att=="courseno":
            pass
        else: #integer or float
            query+='%s="",'%att
    sql1 = "select max(courseno) from currtrtmt"
    db=connect()
    cursor = db.cursor()
    result=True
    cno=0
    try:
        cursor.execute(sql1)
        currentMax=cursor.fetchone()[0]
        if currentMax:
            cno=currentMax+1
        else:
            cno=1
        query="insert into currtrtmt set serialno=%d,courseno=%s,%s "%(
                                                    sno,cno,query.strip(","))
        if localsettings.logqueries:
            print query
        cursor.execute(query)

    except Exception,e:
        print e
        result=False
    db.commit()
    cursor.close()
    #db.close()

    return (result, cno)

if __name__ == "__main__":
    write(31720,4,"20081225")
