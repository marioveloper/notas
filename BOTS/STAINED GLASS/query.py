queryInsertUser = f'INSERT INTO user(id, firstname, username, referred_by, invite_link) VALUES (?, ?, ?, ?, ?)'

queryInsertInvestment = f'INSERT INTO investments(date, user_id) VALUES (?, ?)'

querySelectUser = f'SELECT id, firstname, username, invite_link, rank, wallet FROM user WHERE id = ?'

querySelectInvestment = f'SELECT id, date, user_id FROM investments'

querySelectReferrals = 'SELECT firstname, username, status FROM user WHERE referred_by = ? and status = 1 ORDER BY status desc'

queryUpdateWallet = f'UPDATE user SET wallet = ? WHERE id = ?'

