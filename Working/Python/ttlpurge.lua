function purge_ttl_zero(rec)
	if record.ttl(rec) ~= 0 then
		aerospike:remove(rec)
	end
end
