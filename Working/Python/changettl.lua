function change_ttl(rec)
	  local rec_ttl = record.ttl(rec)
	    if rec_ttl > 315360000 then
		        record.set_ttl(rec, 315360000)
			    aerospike:update(rec)
			      end
		      end
