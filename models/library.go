package models

import (
	modelcore "github.com/sweetrpg/model-core/models"
)

// Library model.
// This model represents a library of RPG resources that belongs to a user.
type Library struct {
	ID     string          `bson:"_id" json:"id" jsonapi:"primary,library"`
	UserID string          `bson:"user_id" json:"user_id" jsonapi:"relation,user"`
	Notes  string          `json:"notes" jsonapi:"attr,notes"`
	Tags   []modelcore.Tag `json:"tags" jsonapi:"attr,tags"`
	modelcore.Auditable
}
